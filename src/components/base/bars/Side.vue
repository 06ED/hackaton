<template>
  <div class="side">

  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .side {
    transition: .4s;
    height: 100vh;
    position: fixed;
    width: 100px;
    background-color: bisque;
    box-shadow: 2px 0 15px 0 grey;
  }
  .side:hover {
    transition: .4s;
    width: calc(100px + 5%);
  }
</style>