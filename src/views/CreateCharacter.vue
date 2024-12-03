<template>
    <div class="createCharacter-page">
        
        <div class="fixed-grid has-6-cols">
            <div class="grid">
                <div class="cell is-col-start-3 mb-6 mt-6">
                    <h1 class="title">Crear Personaje</h1>
                </div>
                <div class="cell is-col-start-3 mt-3">
                    <h2 class="subtitle">Nombre</h2>
                    <input  class="input mb-5" type="text">
                </div>
                    <div class="dropdown is-hoverable cell is-col-start-3">
                        <div class="dropwdown-trigger">
                            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span>Trasfondo</span>
                                <span class="icon is-small">
                                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                                </span>
                            
                            </button>
                        </div>
                        <div class="dropdown-menu" id="dropdown-menu" role="menu">
                            <div class="dropdown-content">
                                <a class="dropdown-item"> Trasfondo </a>
                                <a class="dropdown-item"> Other dropdown item </a>
                                <a class="dropdown-item "> Active dropdown item </a>
                                <a  class="dropdown-item"> Other dropdown item </a>
                                <a class="dropdown-item"> With a divider </a>
                            </div>
                        </div>
                    </div>
                    <div class="dropdown is-hoverable cell is-col-start-3">
                        <div class="dropwdown-trigger">
                            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span>Estilo Marcial</span>
                                <span class="icon is-small">
                                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                                </span>
                            
                            </button>
                        </div>
                        <div class="dropdown-menu" id="dropdown-menu" role="menu">
                            <div class="dropdown-content">
                                <a href="#" class="dropdown-item"> Dropdown item </a>
                                <a class="dropdown-item"> Other dropdown item </a>
                                <a href="#" class="dropdown-item "> Active dropdown item </a>
                                <a href="#" class="dropdown-item"> Other dropdown item </a>
                                <hr class="dropdown-divider" />
                                <a href="#" class="dropdown-item"> With a divider </a>
                            </div>
                        </div>
                    </div>
                    <div class="dropdown is-hoverable cell is-col-start-3">
                        <div class="dropwdown-trigger">
                            <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                                <span>Oficio</span>
                                <span class="icon is-small">
                                    <i class="fas fa-angle-down" aria-hidden="true"></i>
                                </span>
                            
                            </button>
                        </div>
                        <div class="dropdown-menu" id="dropdown-menu" role="menu">
                            <div class="dropdown-content">
                                <a href="#" class="dropdown-item"> Dropdown item </a>
                                <a class="dropdown-item"> Other dropdown item </a>
                                <a href="#" class="dropdown-item "> Active dropdown item </a>
                                <a href="#" class="dropdown-item"> Other dropdown item </a>
                                <hr class="dropdown-divider" />
                                <a href="#" class="dropdown-item"> With a divider </a>
                            </div>
                        </div>
                    </div>
                
                    <div class="buttons cell is-col-start-4 ">
                <router-link to="/create-character/background" class="button is-info">Siguiente</router-link>
                </div>
              

                </div>
            </div>
    
    </div>
</template>

<script>
import axios from 'axios'
    export default {
        name: 'CreateCharacter',
    }
</script>