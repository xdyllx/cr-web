<!--<template>-->
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
<!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</template>-->

<!--<script>-->
<!--import HelloWorld from './components/HelloWorld.vue'-->

<!--export default {-->
<!--  name: 'App',-->
<!--  components: {-->
<!--    HelloWorld-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--  font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--  margin-top: 60px;-->
<!--}-->
<!--</style>-->

<template>
  <div class="common-layout">
    <el-container>
      <el-header>Reco Code Review</el-header>
      <el-main>
        <div class="task-list">
      <table style="width:100%; text-align:center;">
        <thead>
          <tr>
            <th>cr</th>
            <th>发起者</th>
            <th>简介</th>
            <th>创建时间</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="task in info" :key="task.id">
            <td>{{ task.url }}</td>
            <td>{{ task.owner }}</td>
            <td>{{ task.intro }}</td>
            <td>{{ task.created_time }}</td>
            <td>
              <el-button type="primary" round>编辑</el-button>
              <el-button type="info" round disabled>废弃</el-button>
            </td>
          </tr>
        </tbody>
       </table>
    </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: 'App',
        data: function () {
            return {
                info: ''
            }
        },
        mounted() {
            axios
                .get('/api/task')
                .then(response => (this.info = response.data))
        }
    }
</script>

<style>
header {
  background-color: #f2f2f2;
  border-bottom: 1px solid #ddd;
  padding: 10px 20px;
}
</style>
