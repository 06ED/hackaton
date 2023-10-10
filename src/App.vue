<template>
  <div class="app">
<!--  Шапка  -->
    <Side/>
    <Menu/>
<!--  Wrapper  -->
    <wrapper>
      <router-view></router-view>
    </wrapper>
  </div>
</template>

<script>
import Menu from "@/components/base/bars/Menu.vue";
import Wrapper from "@/components/app/Wrapper.vue";
import Side from "@/components/base/bars/Side.vue";

export default {
  components: {Side, Wrapper, Menu}

}
</script>

<style>

  @import url('https://fonts.googleapis.com/css2?family=Prompt&display=swap');
  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Prompt', sans-serif;
  }

</style>