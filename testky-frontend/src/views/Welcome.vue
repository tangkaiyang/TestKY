<template>
  <div class="welcome">
    <img alt="Vue logo" src="../assets/logo.png">
    // #t 类似函数,HelloWorld(msg="Welcome to ...")
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <button @click="greet">Greet</button>
  </div>
</template>

<script>
// @ is an alias to /src
// 引入vue文件
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  // todo 暂时当作无用处理
  name: 'welcome',
  // BOM层根据文件路径硬导入组件component
  components: {
    HelloWorld
  },
  data() {
    return {
      name: 'Vue.js'
    }
  },
  methods: {
    greet(event) {
      alert(`Hello ${this.name}`)
      if (event) {
        alert(event.target.tagName)
      }
    }
  }
}
</script>
