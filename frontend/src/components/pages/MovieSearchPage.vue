<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">영화 검색</div>
        <MovieSearchForm 
          @submitByKeyword="searchMovies"
        />
        <v-select
          v-model="sortingKey"
          ref="sortingKeySelectBox"
          :items="sortingKeys"
          label="정렬 기준을 선택하세요."
          solo
        ></v-select>
      </v-flex>

      <!-- 검색 결과 -->
      <v-flex xs7>
        <v-btn large color="red white--text" @click="sortMoviesByViews">Views</v-btn>
        <v-btn large color="red white--text" @click="sortMoviesByScores">Scores</v-btn>
        <MovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapMutations, mapActions } from "vuex";
import MovieSearchForm from "../MovieSearchForm";
import MovieList from "../MovieList";


export default {
  components: {
    MovieList,
    MovieSearchForm
  },
  data: () => ({
    sortingKeys: ['평점', '조회수'],
    sortingKey: ''
  }),
  computed: {
    ...mapState({
      movieList: state => state.movie.movieSearchList
    }),
  },
  watch: {
    sortingKey: function() {
      this.sortMovies('v')
    }
  },
  methods: {
    ...mapActions("movie", ["searchMovies"]),
    ...mapMutations("movie", ["sortMovies"]),
    sortMoviesByViews() {
      this.sortMovies('v')
    },
    sortMoviesByScores() {
      this.sortMovies('r')
    },
  }
};
</script>
