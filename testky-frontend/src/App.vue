<!--固定格式-->
<template>
  <div id="app">
    <div id="nav">
<!--      #e router-link-->
<!--      实现路由的跳转-->
      <router-link to="/">Home</router-link>
      |
      <router-link to="/about">About</router-link>
      |
      <router-link to="/welcome">Welcome</router-link>
    </div>
<!--    #d 根据路由path匹配router-link,在该位置替换对应组件-->
<!--    #d 根据router-link的to属性在router.js中找到对应的compnent在此处渲染-->
    <router-view/>
  </div>
</template>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
