<template>
  <div class="repo-table">
    <table>
      <thead>
        <tr>
          <th>项目名称</th>
          <th>作者</th>
          <th>语言</th>
          <th>星标数</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="repo in repos" :key="repo.id">
          <td>{{ repo.title }}</td>
          <td>{{ repo.author }}</td>
          <td>{{ repo.language }}</td>
          <td>{{ repo.stars }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue'
const repos = ref([])

const fetchData = async () => {
  const resp = await fetch('http://localhost:8000/repos/filter')
  const data = await resp.json()
  repos.value = data
}

onMounted(() => {
  fetchData()
})
</script>

<style scoped>
.repo-table {
  width: 100%;
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f5f5f5;
}
</style>