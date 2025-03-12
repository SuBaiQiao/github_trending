<template>
  <div class="sidebar">
    <h2>GitHub Trending</h2>
    <ul>
      <li><router-link to="/">项目精选</router-link></li>
      <li><router-link to="/settings">系统设置</router-link></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AppSidebar',
}
</script>

<style scoped>
.sidebar {
  width: 200px;
  height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
}

h2 {
  margin-bottom: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  text-decoration: none;
  color: #2c3e50;
}

a:hover {
  color: #42b983;
}
</style>