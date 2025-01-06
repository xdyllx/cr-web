<template>

   <div class="common-layout">
    <el-container>
      <el-header>
        <div style=" height: 60px; line-height: 60px">
          <span >RECO CODE REVIEW</span>
          <span ref="userHeader" style="float:right" ></span>
        </div>
      </el-header>
      <el-main>
        <div class="button-group">
          <div class="left-button">
            <el-button type="primary" @click="showCreateCrForm">
              新增 code review
            </el-button>
          </div>

          <div class="right-buttons">
            <el-checkbox v-model="showMySelf" label="只看我的" size="large" style=""  @change="resetTaskList" />
            <el-select
              v-model="timeSelect"
              placeholder="cr时间"
              style="width: 200px"
              size="large"
              @change="resetTaskList"
            >
              <el-option
                v-for="item in timeSelectOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
            <el-select
              v-model="statusSelect"
              multiple
              placeholder="cr状态"
              style="width: 200px"
              size="large"
              @change="resetTaskList"
            >
              <el-option
                v-for="item in statusSelectOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </div>
        </div>

        <div>
          <el-table :data="tableData" border style="width: 100%" :row-class-name="tableRowClassName"
                    :header-cell-style="{backgroundColor: '#f2f2f2'}">
            <el-table-column prop="url" label="链接" width="250" >
              <template #default="scope">
                <el-link :href="scope.row.url" target="_blank" rel="noopener noreferrer">{{scope.row.url}}</el-link>
              </template>
            </el-table-column>
            <el-table-column prop="intro" label="简介" width="300" />
            <el-table-column prop="owner" label="发起人" width="150" />
            <el-table-column prop="created_time" label="时间" width="250" />
            <el-table-column prop="status_display" label="状态" width="100" />
            <el-table-column prop="reviewer" label="reviewer" width="150" />
            <el-table-column prop="reviewer_note" label="建议随记" />
            <el-table-column>
            <template #default="scope">
              <el-button size="small" type="primary" @click="showEditCrForm(scope.$index, scope.row)" :disabled="disableOperation(scope.row)">
                编辑
              </el-button>
              <el-button
                size="small" type="danger"
                @click="modifyTaskStatus(scope.$index, scope.row, 5, '废弃')"
                :disabled="disableOperation(scope.row)"
              >
                废弃
              </el-button>
            </template>
            </el-table-column>

            <el-table-column v-if = "showReviewerCol">
            <template #default="scope">
              <el-button size="small" type="primary" @click="modifyTaskStatus(scope.$index, scope.row, 2, '承接')" :disabled="disableAccept(scope.row)">
                承接
              </el-button>
              <el-button size="small" type="success" @click="modifyTaskStatus(scope.$index, scope.row, 3, '通过')" :disabled="disableReviewerOperation(scope.row)">
                通过
              </el-button>
              <el-button
                size="small" type="danger" @click="modifyTaskStatus(scope.$index, scope.row, 4, '驳回')" :disabled="disableReviewerOperation(scope.row)"
              >
                驳回
              </el-button>
              <el-button
                size="small" type="primary" @click="showEditNoteForm(scope.row)"
              >
                编辑建议
              </el-button>
            </template>
            </el-table-column>

          </el-table>


        </div>
      </el-main>
    </el-container>
  </div>




  <el-dialog
    v-model="showCreateCrDiagLog"
    title="新增 code review"
    width="500"
  >
    <el-form :model="cr_form" ref="cr_form" label-width="auto" style="max-width: 600px" :rules="formRules">
    <el-form-item label="cr 链接">
      <el-input v-model="cr_form.url" />
    </el-form-item>
      <el-form-item label="简介">
      <el-input v-model="cr_form.intro" />
    </el-form-item>
  </el-form>

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeCreateCrForm">Cancel</el-button>
        <el-button type="primary" @click="submitCreateCr">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>

    <el-dialog
    v-model="showEditCrDiagLog"
    title="编辑 code review"
    width="500"
  >
    <el-form :model="edit_form" ref="edit_form" label-width="auto" style="max-width: 600px">
    <el-form-item label="cr 链接">
      <el-input v-model="edit_form.url" />
    </el-form-item>
      <el-form-item label="简介">
      <el-input v-model="edit_form.intro" />
    </el-form-item>
  </el-form>

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeEditCrForm">Cancel</el-button>
        <el-button type="primary" @click="submitEditCr">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>

  <el-dialog
    v-model="showEditCrNoteDiagLog"
    title="编辑建议"
    width="500"
  >
    <el-form :model="edit_note_form" ref="edit_note_form" label-width="auto" style="max-width: 600px">
    <el-form-item label="cr 链接">
      <el-input v-model="edit_note_form.url" disabled />
    </el-form-item>
      <el-form-item label="简介">
      <el-input v-model="edit_note_form.intro" disabled />
    </el-form-item>
      <el-form-item label="建议随记">
      <el-input v-model="edit_note_form.reviewer_note" />
    </el-form-item>
  </el-form>

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeEditNoteForm">Cancel</el-button>
        <el-button type="primary" @click="submitEditNote">
          Confirm
        </el-button>
      </div>
    </template>
  </el-dialog>

</template>

<script>
import axios from 'axios';

import {reactive, ref} from "vue";
import {ElMessage, ElMessageBox, FormRules} from "element-plus";

export default {
      name: 'App',

      data: function () {
        return {
          tableData: [],
          showCreateCrDiagLog: false,
          showEditCrDiagLog: false,
          showEditCrNoteDiagLog: false,
          cr_form : reactive({
            url : '',
            intro : ''
          }),
          edit_form : reactive({
            url : '',
            intro : '',
            id: -1
          }),
          edit_note_form : reactive({
            url : '',
            intro : '',
            reviewer_note : '',
            id: -1
          }),
          admin : false,
          showReviewerCol: false,
          username: '',
          showMySelf: false,
          timeSelectOptions: [
            {value: -1, label: '全部'},
            {value: 30, label: '最近一个月'},
            {value: 7, label: '最近一周'},
            {value: 1, label: '最近一天'},
          ],
          timeSelect: 7,
          statusSelectOptions: [
            {value: 1, label: '待处理'},
            {value: 2, label: '进行中'},
            {value: 3, label: '已通过'},
            {value: 4, label: '已驳回'},
            {value: 5, label: '已废弃'},
          ],
          statusSelect: [],

          formRules : reactive({
            url : [{ required: true, message: '请输入 cr 链接', trigger: 'blur' }],
            intro: [{ required: true, message: '请输入简介', trigger: 'blur' }],
          }),
        }
      },
      mounted() {
        let data = {
            'condition': this.getCondition()
          };
        axios
            .post('/api/task', data)
            .then(response => {
              this.username = response.data.username;
              this.$refs.userHeader.innerText = '欢迎,' + this.username;
              console.log(response.data);
              this.tableData = response.data.cr_data;
              this.admin = response.data.admin;
              this.showReviewerCol = this.admin;
            })
            .catch(error => {
              console.log(error);
            })
      },
      methods: {
        tableRowClassName({row, rowIndex}) {
          if (row.status === 3) {
            return 'success-row'
          } else if (row.status === 4 || row.status === 5) {
            return 'finish-row'
          } else if (row.status === 2) {
            return 'accepting-row'
          }
          return ''
        },

        resetCreateCrForm() {
          this.cr_form.url = '';
          this.cr_form.intro = '';
        },

        submitCreateCr() {
          console.log(this.cr_form); // 提交表单
          this.$refs.cr_form.validate((valid) => {
            if (valid) {
              let data = {
                'url': this.cr_form.url,
                'intro': this.cr_form.intro,
                'condition': this.getCondition()
              };
              axios.post('/api/add_task', data)
                  .then(response => {
                    this.tableData = response.data;
                    console.log(this.info);
                    this.closeCreateCrForm();
                    this.showMessage('创建成功');
                  })
            } else {
              console.log("校验失败");
              return false;
            }
          });
        },
        showCreateCrForm() {
          this.resetCreateCrForm();
          this.showCreateCrDiagLog = true;
        },
        closeCreateCrForm() {
          this.showCreateCrDiagLog = false;
          this.resetCreateCrForm();
        },

        showEditCrForm(index, row) {
          this.showEditCrDiagLog = true;
          this.edit_form.url = row.url;
          this.edit_form.intro = row.intro;
          this.edit_form.id = row.id;
        },

        closeEditCrForm() {
          this.showEditCrDiagLog = false;
        },
        submitEditCr() {
          this.$refs.edit_form.validate((valid) => {
            if (valid) {
              let data = {
                'id': this.edit_form.id,
                'url': this.edit_form.url,
                'intro': this.edit_form.intro,
                'condition': this.getCondition()
              };
              axios.post('/api/edit_task', data)
                  .then(response => {
                    this.tableData = response.data;
                    this.closeEditCrForm();
                    this.showMessage('编辑成功');
                  })
            } else {
              console.log("校验失败");
              return false;
            }
          });
        },

        showEditNoteForm(row) {
          this.showEditCrNoteDiagLog = true;
          this.edit_note_form.url = row.url;
          this.edit_note_form.intro = row.intro;
          this.edit_note_form.reviewer_note = row.reviewer_note;
          this.edit_note_form.id = row.id;
        },

        closeEditNoteForm() {
          this.showEditCrNoteDiagLog = false;
        },
        submitEditNote() {
          this.$refs.edit_note_form.validate((valid) => {
            if (valid) {
              let data = {
                'id': this.edit_note_form.id,
                'reviewer_note': this.edit_note_form.reviewer_note,
                'condition': this.getCondition()
              };
              axios.post('/api/edit_task', data)
                  .then(response => {
                    this.tableData = response.data;
                    this.closeEditNoteForm();
                    this.showMessage('编辑成功');
                  })
            } else {
              console.log("校验失败");
              return false;
            }
          });
        },


        modifyTaskStatus(index, row, status, op_name) {
          let data = {'id': row.id, 'status': status, 'condition': this.getCondition()};
          ElMessageBox.confirm(
            `确认${op_name}该cr吗`,
            '提示',
            {
              confirmButtonText: '确认',
              cancelButtonText: '取消',
              type: 'warning',
            }
          )
            .then(() => {
              axios.post('/api/modify_task_status', data)
                    .then(response => {
                      this.tableData = response.data;
                      this.showMessage(`${op_name}成功`);
                    })
            })
            .catch(() => {
            });
        },

        disableOperation(row) {
          if (row.status === 3 || row.status === 4 || row.status === 5) {
            return true;
          }
          return row.owner !== this.username;
        },

        disableAccept(row) {
          if (row.status !== 1) {
            return true;
          }
          return false;
        },

        disableReviewerOperation(row) {
          if (row.status !== 2 || row.reviewer !== this.username) {
            return true;
          }
          return false;
        },

        resetTaskList() {
          let data = {
            'condition': this.getCondition()
          }
          axios
            .post('/api/task', data)
            .then(response => {
              this.tableData = response.data.cr_data;
            })

        },

        getCondition() {
          return {'timeSelect': this.timeSelect, 'statusSelect': this.statusSelect, 'showMySelf': this.showMySelf}
        },

        showMessage(msg) {
          ElMessage({
            type: 'success',
            message: msg,
          })
        }
      }
    }
</script>

<style>

  .button-group {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }

  .left-button {
    order: 1;
  }

  .right-buttons {
    display: flex;
    justify-content: flex-end;
    order: 2;
    gap: 20px;
  }

.el-header {
  background-color: #f2f2f2;
  border-bottom: 1px solid #ddd;
  padding: 10px 20px;
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}
.el-table .finish-row {
  --el-table-tr-bg-color: rgb(245,245,245);
}
.el-table .accepting-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
</style>
