<template>
    <div class="home">
      <div class="columns is-multiline">
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Characters</h2>
        </div>

      </div>

      <div class="column is-1" 
      v-for="character in characters"
      v-bind:key="character.id">
        <div class="box box-color-is-red"> 
        <figure class="image mb-4">
            <img v-bind:src="character.get_thumbnail">
        </figure>

        <h3 class="is-size-4">{{ character.name }}</h3>
        <h3 class="is-size-6 has-text-grey">{{ character.level }}</h3>
        <router-link v-bind:to="character.get_absolute_url" class="button is-dark mt-4">View details</router-link>
        </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      characters: []
    }
  },
  components: {

  },
  mounted() {
    this.getCharacters()
    
    document.title = 'Characters'
  },
  methods: {
    getCharacters() {
      
        axios
        .get('/api/v1/characters/')
        .then(response => {
          this.characters = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}

</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
