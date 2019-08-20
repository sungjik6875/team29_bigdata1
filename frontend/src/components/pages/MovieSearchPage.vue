<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs6>
        <div class="display-2 pa-10">영화 검색</div>
        <MovieSearchForm 
          @submitByName="searchMovies"
          @submitByGenre="searchMovies"
        />
      </v-flex>
      <!-- 검색 결과 -->
      <v-flex xs7>
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
  data: () => ({}),
  computed: {
    ...mapState({
      movieList: state => state.movie.movieSearchList
    })
  },
  methods: {
    ...mapActions("movie", ["searchMovies"]),
  }
};
</script>
