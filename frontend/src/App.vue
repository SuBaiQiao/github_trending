<template>
  <div class="app-container">
    <Sidebar />
    <div class="content">
      <RouterView style="height: 100% !important" />
    </div>
  </div>
</template>

<script setup>
import Sidebar from "@/components/Sidebar.vue";
</script>

<style>
.app-container {
  display: flex;
  height: 100vh;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>
