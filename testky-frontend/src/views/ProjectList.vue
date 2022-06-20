<template>
  <div class="project_list">
    <button @click="test_get">GET</button>
    <button @click="test_post">POST</button>
  </div>
</template>

<script>
// import axios from 'axios'
const axios = require('axios').default;
export default {
  name: "ProjectList",
  methods: {
    test_get() {
      axios.get('http://localhost:8000/get/?a=1&b=2').then(function (response) {
        console.log(response);
        console.log(response.data);
      })
    },
    test_post() {
      axios.post('http://localhost:8000/post/', {
        'a': 11,
        'b': 22
      }).then(function (response) {
        console.log(response);
        console.log(response.data);
      })
    }
  },
  mounted() {
    console.log('-------mounting-------');
    this.test_get();
    this.test_post();
    console.log('-------mounted-------');
  }
}
</script>

<style scoped>

</style>