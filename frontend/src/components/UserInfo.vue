<template>
  <!-- 해당 사용자가 존재할 경우 -->
  <div v-if="_props.username">
    <div class="user-info-container">
      <div class="user-info-title"> Profile </div>
      <div><i class="fas fa-user"></i> {{ username }}</div>
      <div>
        <div v-if="gender==='M'"><i class="fas fa-mars"></i> {{ age }}</div>
        <div v-else><i class="fas fa-venus"></i> {{ age }}</div>
      </div>
      <div>{{ occupation }}</div>
    </div>
    <div class="user-info-container">
      <div class="user-info-title"> 해당 유저가 관람한 영화 </div>
      <ul>
        <li v-for="movie in movies">
          {{ movie }}
        </li>
      </ul>
    </div>
  </div>

  <!-- 해당 사용자가 존재하지 않을 경우 -->
  <div v-else>
    <div class="user-info-title"></div>
  </div>
</template>

<script>
export default {
  props: ['username', 'gender', 'age', 'occupation', 'movies']
}
</script>

<style scoped lang="scss">
.user-info-container {
  &:first-of-type {
    margin: 3vh 0 3vh 0;
    padding: 5% 0 5% 0;
    border-style: solid;
    border-color: black;
    border-width : 3px 0 3px 0;
  }
}

.user-info-title {
  margin-bottom: 5vh;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 1.5rem;
}

ul > li {
  margin-bottom: 1vh;
  padding: 1vh 0;
  border-radius: 5px;
  box-shadow: 1px 1px 3px grey;
  font-family: 'Lato', sans-serif;
  transition: all 1s;
  &:hover {
    background-color: rgb(83, 118, 194);
    box-shadow: 1px 1px 5px grey;
    color: whitesmoke;
  }
}
</style>