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

        <div>
    <el-button type="primary" @click="showCreateCrForm">添加任务</el-button>

  </div>



      </el-main>
    </el-container>
  </div>


      <el-dialog
      title="添加任务" style="width: 400px"
      v-bind:visible="showCreateCrDiagLog">
      <!--:before-close="handleClose" -->
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="任务 URL">
          <el-input v-model="form.url" placeholder="请输入任务 URL"></el-input>
        </el-form-item>
        <el-form-item label="任务简介">
          <el-input v-model="form.description" placeholder="请输入任务简介"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="resetCreateCrForm">取消</el-button>
          <el-button type="primary" @click="submitForm">提交</el-button>
      </el-form-item>
      </el-form>

    </el-dialog>
</template>

<script>
import axios from 'axios';

    export default {
      name: 'App',
      // setup() {
      //   const showCreateCrDiagLog = ref<Boolean>false;
      //
      // },
      data: function () {
        return {
          info: '',
          showCreateCrDiagLog: false
        }
      },
      mounted() {
        axios
            .get('/api/task')
            .then(response => (this.info = response.data))
      },
      methods: {
        resetCreateCrForm() {
          this.$refs.form.resetFields();
        },
        // handleClose(done) {
        //   this.$confirm("确认关闭？")
        //       .then(_ => {
        //         done();
        //       })
        //       .catch(_ => {
        //       });
        // },
        submitForm() {
          this.$refs.form.validate((valid) => {
            if (valid) {
              console.log(this.form); // 提交表单
              this.showCreateCrDiagLog = false;
              this.resetCreateCrForm();
            } else {
              console.log("校验失败");
              return false;
            }
          });
        },
        showCreateCrForm() {
          this.showCreateCrDiagLog = true;
        }
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
