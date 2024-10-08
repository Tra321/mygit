<template>
    <div class="manage">
        <el-dialog
            title="提示"
            :visible.sync="dialogVisible"
            width="50%"
            :before-close="handleClose">
            <!-- 用户的表单信息 -->
            <el-form ref="form" :rules="rules" :inline="true" :model="form" label-width="80px">
                <el-form-item label="姓名" prop="name">
                    <el-input placeholder="请输入姓名" v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="年龄" prop="age">
                    <el-input placeholder="请输入年龄" v-model="form.age"></el-input>
                </el-form-item>
                <el-form-item label="性别" prop="sex">
                    <el-select v-model="form.sex" placeholder="请选择">
                        <el-option label="男" :value="1"></el-option>
                        <el-option label="女" :value="0"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="出生日期" prop="birth">
                    <el-date-picker
                        v-model="form.birth"
                        type="date"
                        placeholder="选择日期"
                        value-format="yyyy-MM-DD">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="地址" prop="addr">
                    <el-input placeholder="请输入地址" v-model="form.addr"></el-input>
                </el-form-item>
            </el-form>

            <span slot="footer" class="dialog-footer">
                <el-button @click="cancel">取 消</el-button>
                <el-button type="primary" @click="submit">确 定</el-button>
            </span>
        </el-dialog>
        <div class="manage-header">
            <el-button @click="handleAdd" type="primary">
                +新增
            </el-button>
            <!-- form搜索区 -->
            <el-form :inline="true" :model="userForm">
                <el-form-item>
                    <el-input placeholder="请输入名称" v-model="userForm.name"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">查询</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div class="common-tabel">
            <el-table
                stripe
                height="90%"
                :data="tableData"
                style="width: 100%">
                <el-table-column
                    prop="name"
                    label="姓名">
                </el-table-column>
                <el-table-column
                    prop="sex"
                    label="性别">
                    <template slot-scope="scope">
                        <span>{{ scope.row.sex == 1 ? '男' : '女' }}</span>
                    </template>
                </el-table-column>
                <el-table-column
                    prop="age"
                    label="年龄">
                </el-table-column>
                <el-table-column
                    prop="birth"
                    label="出生日期">
                </el-table-column>
                <el-table-column
                    prop="addr"
                    label="地址">
                </el-table-column>
                <el-table-column
                    prop="addr"
                    label="地址">
                    <template slot-scope="scope">
                        <el-button size="mini" @click="handleEdit(scope.row)">编辑</el-button>
                        <el-button type="danger" size="mini" @click="handleDelete(scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="pager">
                <el-pagination
                    layout="prev, pager, next"
                    :total="total"
                    @current-change="handlePage">
                </el-pagination>
            </div>
        </div>
    </div>
</template>
<script>
import { getUser, addUser, editUser, delUser } from '../api'
export default {
    data() {
        return {
            dialogVisible: false,
            form: {
                name: '',
                age: '',
                sex: '',
                birth: '',
                addr: '',
            },
            rules: {
                name:[
                    { required: true, message: '请输入姓名' }
                ],
                age: [
                    { required: true,message: '请输入年龄'}
                ],
                sex: [
                    { required: true,message: '请选择性别'}
                ],
                birth: [
                    { required: true,message: '请选择出生日期'}
                ],
                addr: [
                    { required: true,message: '请输入地址'}
                ],
            },
            tableData: [],
            modalType: 0, // 0表示新增的弹窗， 1表示编辑
            total: 0, // 当前的众条数
            pageData: {
                page: 1,
                limit: 10
            },
            userForm: {
                name: ''
            }
        }
    },
    methods: {
        // 提交用户表单
        submit() {
            this.$refs.form.validate((valid) => {
                if (valid) {
                    // 后续对表单数据的处理
                    if (this.modalType === 0) {
                        addUser(this.form).then(() => {
                            // 重新获取列表的接口
                            this.getList()
                        })
                    }else {
                        editUser(this.form).then(() => {
                            // 重新获取列表的接口
                            this.getList()
                        })
                    }

                    // 清空表单的数据
                    this.$refs.form.resetFields()
                    // 关闭弹窗
                    this.dialogVisible = false
                }
            })
        },
        // 弹窗关闭的时候
        handleClose() {
            this.$refs.form.resetFields()
            this.dialogVisible = false
        },
        cancel() {
            this.handleClose()
        },
        handleEdit(row) {
            this.modalType = 1
            this.dialogVisible = true
            // 注意需要对当前行数据进行深拷贝，否则会出错
            this.form = JSON.parse(JSON.stringify(row))
        },
        handleDelete(row) {
            this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    delUser({ id: row.id }).then(() => {
                        this.$message({
                            type: 'success',
                            message: '删除成功!'
                        });
                        // 重新获取列表的接口
                        this.getList()
                    })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });          
            });
        },
        handleAdd() {
            this.modalType = 0
            this.dialogVisible = true
        },
        // 获取列表的数据
        getList() {
             // 获取的列表的数据
            getUser({params: {...this.userForm, ...this.pageData}}).then(({ data }) => {
                console.log(data)
                this.tableData = data.list
                this.total = data.count || 0
            })
        },
        // 选择页码的回调函数
        handlePage(val) {
            // console.log(val, 'val')
            this.pageData.page = val
            this.getList()
        },
        // 列表的查询
        onSubmit() {
            this.getList()
        }
    },
    mounted () {
       this.getList()
    }
}
</script>
<style lang="less" scoped>
.manage {
    height: 90%;
    .manage-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .common-tabel {
        position: relative;
        height: calc(100% - 62px);
        .pager {
            position: absolute;
            bottom: 0;
            right: 20px;
        }
    }
}
</style>