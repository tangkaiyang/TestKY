<template>
  <div class="home">
    <el-container style="height: 100%; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1', '3']">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>导航一</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="1-1">选项1</el-menu-item>
              <el-menu-item index="1-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="1-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <template slot="title">选项4</template>
              <el-menu-item index="1-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>导航二</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="2-1">选项1</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="2-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i>导航三</template>
            <el-menu-item-group>
              <template slot="title">分组一</template>
              <el-menu-item index="3-1">选项1</el-menu-item>
              <el-menu-item index="3-2">选项2</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组2">
              <el-menu-item index="3-3">选项3</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="3-4">
              <template slot="title">选项4</template>
              <el-menu-item index="3-4-1">选项4-1</el-menu-item>
            </el-submenu>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>

        <el-main>
          <div style="display: flex;justify-content: space-evenly;padding-top: 20px">
            <!--            项目总览卡片-->
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>项目总览</span>
                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
              </div>
              <div v-for="o in 4" :key="o" class="text item">
                {{ '列表内容 ' + o }}
              </div>
            </el-card>

            <!--            监控情况卡片-->
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>监控情况</span>
                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
              </div>
              <div>
                <span style="font-size: small">用例通过率</span>
                <el-progress :text-inside="true" :stroke-width="26" :percentage="70"></el-progress>
                <br>
                <span style="font-size: small">接口通过率</span>
                <el-progress :text-inside="true" :stroke-width="24" :percentage="100" status="success"></el-progress>
                <br>
                <span style="font-size: small">用例失败/报错率</span>
                <el-progress :text-inside="true" :stroke-width="22" :percentage="80" status="warning"></el-progress>
                <br>
              </div>
            </el-card>
          </div>

          <div style="display: flex;justify-content: space-evenly;padding-top: 20px">
            <!--            个人贡献卡片-->
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>个人贡献</span>
                <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
              </div>
              <div style="display: flex;justify-content: space-evenly">
                <el-progress type="circle" :percentage="0"></el-progress>
                <el-progress type="circle" :percentage="25"></el-progress>
                <el-progress type="circle" :percentage="100" status="success"></el-progress>
                <el-progress type="circle" :percentage="70" status="warning"></el-progress>
              </div>
            </el-card>
            <!--            消息列表卡片-->
            <el-card class="box-card">
              <div v-for="o in 4" :key="o" class="text item">
                {{ '列表内容 ' + o }}
              </div>
            </el-card>
          </div>
        </el-main>

        <el-footer></el-footer>
      </el-container>
    </el-container>
  </div>
</template>


<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

/*定义el-main布局*/
.el-main {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.el-footer {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

/*卡片样式*/
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}

.box-card {
  min-width: 300px;
  width: 50%;
  margin-left: 15px;
}

/*卡片文本靠左*/
.el-card .text {
  text-align: left;
}

.el-main span {
  float: left;
}
</style>

<script>
export default {};
</script>