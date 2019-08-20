<template>
  <v-form ref="form">
    <v-text-field v-model="keyword" label="키워드를 입력하세요(영화명/장르)" />
    <v-layout justify-center pa-10>
      <v-btn large color="indigo white--text" @click="onSubmitByName">Name</v-btn>
      <v-btn large color="green white--text" @click="onSubmitByGenre">Genres</v-btn>
    </v-layout>
  </v-form>
</template>

<script>
export default {
  data: () => ({
    keyword: ""
  }),
  methods: {
    onSubmitByName: function() {
      const params = {
        title: this.keyword,
        key: "title"
      };
      this.$emit('submitByName', params)
    },
    onSubmitByGenre: function() {
      const params = {
        genre: this.keyword,
        key: "genre"
      };
      this.$emit('submitByGenre', params)
    }
  }
};
</script>