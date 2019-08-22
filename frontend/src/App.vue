<template>
  <v-app id="app">
    <v-app-bar app clipped-left color="indigo">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
      <span class="title ml-3 mr-5 white--text">영화 추천 서비스</span>
      <v-spacer />
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">
        <template v-for="(choice, i) in choices">
          <v-list-item
            :key="i"
            @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
          >
            <v-list-item-action>
              <v-icon>{{ choice.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <div class="content-box">
        <Loader v-if="isLoading"/>
        <div :class="{ isBlind : isLoading }">
          <v-container fluid fill-height class="grey lighten-4">
            <v-layout justify-center align-center>
              <!-- each pages will be placed here -->
              <router-view />
            </v-layout>
          </v-container>
        </div class="content-box">
      </div>
    </v-content>
  </v-app>
</template>

<script>
import { mapState } from 'vuex';
import { eBus } from './api/eventBus';
import Loader from './components/Loader';

export default {
  components: {
    Loader
  },
  data: () => ({
    drawer: null,
    choices: [
      {
        icon: "fas fa-search",
        text: "영화 검색",
        path: "movie-search"
      },
      { 
        icon: "mdi-face",
        text: "사용자 찾기",
        path: "user-info"
      },
      { 
        icon: "mdi-movie",
        text: "영화 상세 페이지",
        path: 'movie-info'
      }
    ]
  }),
  methods: {
    goTo: function(path) {
      this.$router.push({ name: path });
    }
  },
  computed: {
    ...mapState('app', ['isLoading'])
  },
  created() {
    eBus.$on('goToMovieDetail', (movieId) => {
      this.$router.push({ 
        name: 'movie-info',
        query: { 
          movieId 
        }
      })
    })
  },
  destroyed() {
    eBus.$off('goToMovieDetal')
  },
};
</script>

<style>
ul li {
 list-style-type: none;
}

#keep .v-navigation-drawer__border {
  display: none;
}

.isBlind {
  opacity: 0.5;
}

.content-box {
  margin: 0 auto;
  position: relative;
}
</style>