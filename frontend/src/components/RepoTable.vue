<template>
  <a-spin
    :spinning="loading"
    tip="正在努力获取数据..."
    style="max-height: 100% !important"
  >
    <div>
      <a-segmented
        v-model:value="selectedType"
        :options="typeOptions"
        style="margin-right: 16px"
      ></a-segmented>
    </div>
    <div class="repo-table">
      <table>
        <thead>
          <tr>
            <th>序号</th>
            <th>项目名称</th>
            <th>作者</th>
            <th>语言</th>
            <th>星标数</th>
            <th>保存日期</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(repo, index) in repos" :key="repo.id">
            <td>{{ (pageNum - 1) * pageSize + index + 1 }}</td>
            <td>{{ repo.title }}</td>
            <td>{{ repo.author }}</td>
            <td>{{ repo.language }}</td>
            <td>{{ repo.stars }}</td>
            <td>{{ dayjs(repo.created_at).format("YYYY-MM-DD") }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top: 10px">
      <span style="margin-right: 20px">总条数：{{ total }}</span>
      <span
        @click="pageNumChange(item)"
        :class="['pageSize', item === pageNum ? 'active' : '']"
        v-for="item in count_limit"
        :key="item"
        >{{ item }}</span
      >
    </div>
  </a-spin>
</template>

<script setup>
import { onMounted, ref, watchEffect } from "vue";
import { message } from "ant-design-vue";
import dayjs from "dayjs";

const repos = ref([]);
const count_limit = ref(0);
const pageSize = ref(20);
const pageNum = ref(1);
const total = ref(0);
const selectedType = ref("日");
const typeOptions = ["日", "周", "月"];
const loading = ref(false);

const fetchData = async () => {
  loading.value = true;
  try {
    let type;
    switch (selectedType.value) {
      case "日":
        type = "daily";
        break;
      case "周":
        type = "weekly";
        break;
      case "月":
        type = "monthly";
        break;
      default:
        type = "daily";
    }
    const params = new URLSearchParams({
      limit: pageSize.value,
      offset: pageSize.value * (pageNum.value - 1) + 1,
      type: type,
    });
    const resp = await fetch(`http://localhost:8000/repos/filter?${params}`);
    const data = await resp.json();
    if (data.code === 1) {
      count_limit.value = data.data.count_limit;
      total.value = data.data.count;
      repos.value = data.data.data;
    } else {
      message.error("请求数据失败," + data.message);
    }
  } catch (error) {
    message.error("请求数据失败");
  } finally {
    loading.value = false;
  }
};

const pageNumChange = (item) => {
  pageNum.value = item;
};

watchEffect(() => {
  fetchData();
});

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
.repo-table {
  width: 100%;
  padding: 20px;
  height: calc(100vh - 32px - 27px - 40px);
  overflow-y: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f5f5f5;
}

table tbody th,
td {
  cursor: pointer;
}

.pageSize {
  margin-right: 10px;
  cursor: pointer;
}

.pageSize.active {
  color: #3b8dff;
}
</style>
