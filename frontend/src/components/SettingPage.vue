<template>
  <a-spin
    :spinning="loading"
    tip="正在努力获取数据..."
    style="max-height: 100% !important"
  >
    <div class="setting-page">
      <!-- 选择框 -->
      <div>
        <a-segmented
          v-model:value="selectedPeriod"
          :options="periodOptions"
          style="margin-right: 16px"
        ></a-segmented>
      </div>
      <!-- 按钮 -->
      <div>
        <a-button @click="fetchDataByPeriod" :loading="loading"
          >获取数据</a-button
        >
      </div>
    </div>
  </a-spin>
</template>

<script setup>
import { ref } from "vue";
import { message } from "ant-design-vue";

// 定义选择框选项
const periodOptions = ["日", "周", "月"];
// 绑定选择框选中的值
const selectedPeriod = ref("日");
const loading = ref(false);
// 点击按钮调用后端接口的函数
const fetchDataByPeriod = async () => {
  try {
    // 根据选择的周期构建请求参数
    let period;
    switch (selectedPeriod.value) {
      case "日":
        period = "daily";
        break;
      case "周":
        period = "weekly";
        break;
      case "月":
        period = "monthly";
        break;
      default:
        period = "daily";
    }
    loading.value = true;
    // 调用后端接口
    const response = await fetch(`http://localhost:8000/${period}-repos`);
    const data = await response.json();
    if (data.code === 1) {
      // 处理数据
      message.success("数据获取成功");
    } else {
      message.error("请求数据失败:", data.message);
    }
  } catch (error) {
    message.error("请求数据失败:", error);
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.setting-page {
  padding: 20px;
  display: flex;
  align-items: center;
}
</style>
