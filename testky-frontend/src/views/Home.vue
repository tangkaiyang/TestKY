<template>
  <div class="home">
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
  name: 'home',
  // BOM层根据文件路径硬导入组件component
  components: {
    HelloWorld
  },
  data() {
    return {
      a: 1,
      b: 2,
      _a: 3,
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
  },
  created() {
    console.log(this.$data.a);
    console.log(this.b);
    console.log(this._a);
    console.log(this.$data._a);
  }
}
</script>
