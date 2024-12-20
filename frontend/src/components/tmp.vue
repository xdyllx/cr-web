<template>
  <div class="task-list">
    <div class="header">
      <div class="col-name">任务名</div>
      <div class="col-name">创建者</div>
      <div class="col-name">任务URL</div>
      <div class="col-name">创建时间</div>
      <div class="col-name">操作</div>
    </div>
    <div class="body">
      <div class="row" v-for="task in tasks" :key="task.id">
        <div class="col">{{ task.title }}</div>
        <div class="col">{{ task.creator }}</div>
        <div class="col"><a :href="task.url">{{ task.url }}</a></div>
        <div class="col">{{ task.createTime }}</div>
        <div class="col">
          <button class="edit-btn" @click="editTask(task)">编辑</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [
        { id: 1, title: "任务1", creator: "user1", url: "https://example.com/task1", createTime: "2021-07-01" },
        { id: 2, title: "任务2", creator: "user2", url: "https://example.com/task2", createTime: "2021-07-02" },
        { id: 3, title: "任务3", creator: "user3", url: "https://example.com/task3", createTime: "2021-07-03" },
        { id: 4, title: "任务4", creator: "user4", url: "https://example.com/task4", createTime: "2021-07-04" },
        { id: 5, title: "任务5", creator: "user5", url: "https://example.com/task5", createTime: "2021-07-05" },
      ],
      editingTask: null, // 当前正在编辑的任务
    };
  },
  methods: {
    editTask(task) {
      // 更新正在编辑的任务
      this.editingTask = task;
    },
    saveTaskChanges() {
      // 保存编辑后的任务数据并清空正在编辑的状态
      this.editingTask = null;
    },
    cancelTaskChanges() {
      // 取消编辑，清空正在编辑的状态
      this.editingTask = null;
    },
  },
};
</script>
