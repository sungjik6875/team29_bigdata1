<template>
  <!-- 영화가 있을 때 -->
  <div v-if="movieInfo.id">
    <div>{{ movieInfo.title }}</div>
    <div>{{ movieInfo.genres }}</div>
    <div>{{ movieInfo.viewCnt }}</div>
    <div>{{ movieInfo.rating }}</div>
    <div>
      <p>이 영화를 관람한 유저들</p>
      <ul>
        <li v-for="user in this.userListForMovie">{{ user }}</li>
      </ul>
    </div>
  </div>

  <!-- 영화가 없을 때 -->
  <div v-else>
    <div>영화를 검색해주세요</div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      movieInfo: { 
        type: Object, 
        default: {}
      },
    }
  },
  computed: {
    ...mapState('movie', ['userListForMovie'])
  },
  methods: {
    ...mapActions('movie', ['getMovieInfo'])
  },
  created() {
    // console.log("movieDetail", this.$route.params);
    this.movieInfo = this.$route.params;
    const params = {
      id: this.movieInfo.id
    }
    if (this.movieInfo.id) {
      this.getMovieInfo(params)
    }
  }
}
</script>

<style scoped>

</style>