<template>
  <!-- 해당 사용자가 존재할 경우 -->
  <div v-if="_props.username">
    <div> 유저 정보 </div>
    <div>{{ username }}</div>
    <div>{{ gender }}</div>
    <div>{{ age }}</div>
    <div>{{ occupation }}</div>
    <div> 해당 유저가 관람한 영화 </div>
    <ul>
      <li v-for="movie in movies">
        {{ movie }}
      </li>
    </ul>
  </div>

  <!-- 해당 사용자가 존재하지 않을 경우 -->
  <div v-else>
    <div class="user-info-title">해당 사용자가 존재하지 않습니다.</div>
  </div>
</template>

<script>
export default {
  props: ['username', 'gender', 'age', 'occupation', 'movies']
}
</script>

<style scoped>

</style>