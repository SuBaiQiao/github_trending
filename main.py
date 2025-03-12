from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from models import TrendingRepo, engine
from sqlalchemy.orm import Session
import os

app = FastAPI()

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# 确保数据库连接配置正确
if not engine:
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/github_trending')

@app.get("/repos")
def get_all_repos():
    with Session(engine) as session:
        repos = session.query(TrendingRepo).all()
        return repos

@app.get("/repos/filter")
def filter_repos(
    language: str = Query(None),
    author: str = Query(None),
    stars: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0),
    sort_by: str = Query(None, description="Sort by field (title, author, language, stars)"),
    order: str = Query("asc", description="Sort order (asc or desc)")
):
    with Session(engine) as session:
        query = session.query(TrendingRepo)
        if language:
            query = query.filter(TrendingRepo.language == language)
        if author:
            query = query.filter(TrendingRepo.author == author)
        if stars:
            query = query.filter(TrendingRepo.stars == stars)
        if sort_by:
            if order == "desc":
                query = query.order_by(getattr(TrendingRepo, sort_by).desc())
            else:
                query = query.order_by(getattr(TrendingRepo, sort_by))
        repos = query.offset(offset).limit(limit).all()
        return repos

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from scraper import GitHubTrendingScraper

scheduler = BackgroundScheduler()

# 定义定时任务
@scheduler.scheduled_job('cron', hour=0, minute=40)
def scheduled_scrape():
    print(f'[{datetime.now()}] 开始执行定时任务...')
    scraper = GitHubTrendingScraper()
    repos = scraper.scrape()
    scraper.save_to_database(repos)
    print(f'[{datetime.now()}] 定时任务执行完成')

@app.on_event("startup")
async def startup_event():
    scheduler.start()

@app.get("/weekly-repos")
async def get_weekly_repos():
    try:
        scraper = GitHubTrendingScraper()
        repos = scraper.scrape(type='weekly')
        scraper.save_to_database(repos)
        return {"status": "success", "message": repos}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get('/monthly-repos')
async def get_monthly_repos():
    try:
        scraper = GitHubTrendingScraper()
        repos = scraper.scrape(type='monthly')
        scraper.save_to_database(repos)
        return {"status": "success", "message": repos}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/daily-repos")
async def scrape_and_save():
    try:
        scraper = GitHubTrendingScraper()
        repos = scraper.scrape()
        scraper.save_to_database(repos)
        return {"status": "success", "message": repos}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)