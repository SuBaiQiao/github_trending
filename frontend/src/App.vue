<template>
  <div class="app-container">
    <Sidebar />
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar.vue'
// import RepoTable from './components/RepoTable.vue'
</script>

<style>
.app-container {
  display: flex;
  height: 100vh;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>
