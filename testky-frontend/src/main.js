import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 引入elementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  // createElement
  render: h => h(App)
  // 挂载id=app的标签
}).$mount('#app')
