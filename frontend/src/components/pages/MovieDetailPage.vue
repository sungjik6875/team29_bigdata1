<template>
  <!-- 영화가 있을 때 -->
  <div class="movie-info-page" v-if="movieInfo.id">
    <div class="movie-info-container">
      <div class="movie-info-title">{{ movieInfo.title }}</div>
      <div class="movie-info">{{ parseGenreArrayStr }}</div>
      <div class="movie-info"><i class="fas fa-eye"></i> {{ movieInfo.view_cnt }}</div>
      <div class="movie-info" v-html="drawStarRating"></div>
    </div>
    
    <div class="movie-info-container">
      <div class="movie-info-title">이 영화를 관람한 유저들</div>
      <ul>
        <li :key="`userList${idx}`" v-for="(user, idx) in movieInfo.users" v-if="idx < numberOfUserList">{{ user }}</li>
      </ul>
      <div class="button-container">
        <v-btn 
          large color="indigo white--text"
          v-if="users < movieInfo.users.length" 
          @click="addUserList"
        ><i class="fas fa-plus"></i>
        </v-btn>
      </div>
    </div>
  </div>

  <!-- 영화가 없을 때 -->
  <div class="movie-info-page" v-else>
    <div class="movie-info-title">영화를 검색해주세요</div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  data() {
    return {
      users: 10
    }
  },
  computed: {
    ...mapState('movie', ['movieInfo']),
    parseGenreArrayStr() {
      let genreArrayStr = ''
      for(let i = 0; i < this.movieInfo.genres_array.length; i++) {
        genreArrayStr += this.movieInfo.genres_array[i];
        if (i < this.movieInfo.genres_array.length - 1) {
          genreArrayStr += ' | '
        }
      }
      return genreArrayStr
    },
    drawStarRating() {
      let stars = ''
      const score = this.movieInfo.average_rating;
      for(let i = 1; i < 6; i++) {
        if (i <= score) {
          stars += '<i class="fas fa-star"></i>'
        } else {
          if (i > score + 0.5) {
            stars += '<i class="far fa-star"></i>'
          } else {
            stars += '<i class="fas fa-star-half-alt"></i>'
          }      
        }
      }
      stars += ` <strong>${this.movieInfo.average_rating}</strong>`
      return stars
    },
    numberOfUserList() {
      return this.users
    }
  },
  watch: {
    'movieInfo.title': function() {
      this.users = 10
    }
  },
  methods: {
    addUserList() {
      this.users += 10
    }
  }
}
</script>

<style scoped lang="scss">
.movie-info-page {
  width: 80%;
}

.movie-info-container {
  &:not(last-of-type) {
    margin: 3vh 0 3vh 0;
    padding: 5% 0 5% 0;
    border-style: solid;
    border-color: black;
    border-width : 3px 0 0 0;
  }
}

.movie-info-title {
  margin-bottom: 5vh;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 1.5rem;
  text-align: center;
}

.movie-info {
  margin-bottom: 1vh;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 1rem;
  text-align: center;
}

ul > li {
  margin-bottom: 1vh;
  padding: 1vh 0;
  border-radius: 5px;
  box-shadow: 1px 1px 3px grey;
  font-family: 'Lato', sans-serif;
  text-align: center;
  transition: all 1s;
  &:hover {
    background-color: rgb(83, 118, 194);
    box-shadow: 1px 1px 5px grey;
    color: whitesmoke;
  }
}

.button-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1vh 0;
}
</style>