<template>
  <div id="wrapper"> 

    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Solaris</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="true" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
     
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/create-character" class="button is-light">Create Character</router-link>
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/sign-up" class="button is-light">Sign Up</router-link>
              
            </div>
          
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>
  
  
</div>
</template>

<script>  
  export default {
    data() {
      return {
        showMobileMenu: false,
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
