<template>
    <div class="character-page">
        <div class="columns is-multiline is-centered">
            <div class="fixed-grid has-2-cols column is-4 has-background-grey-light">
                <div class="grid">
                    <div class=" cell fixed-grid has-2-cols">
                        <div class="grid">
                            <div class="cell">
                                <figure class="image mb-1"> 
                                    <img v-bind:src="character.get_thumbnail">
                                </figure>
                                <h1 class="title">{{ character.name }}</h1>
                            </div>
                            <div class="cell">
                                <h2 class="subtitle">Trasfondo</h2>
                                <h2 class="subtitle">Oficio</h2>
                                <h2 class="subtitle">Estilo Marcial</h2>
                                <h2 class="subtitle">Raza</h2>
                                <h2 class="subtitle">Oficio</h2>
                            </div>
                        </div>
                    </div>
                    <div class="cell ">
                        <div class="fixed-grid has-2-cols">
                            <div class="grid">
                                <div class="cell box">
                                    <p>HP</p>
                                </div>
                                <div class="cell box">
                                    <p>HP</p>
                                </div>
                                <div class="cell box">
                                    <p>HP</p>
                                </div>
                                <div class="cell box">
                                    <p>HP actual</p>
                                </div>
                                <div class="cell box ">
                                    <p>Dodge</p>
                                </div>
                                <div class="cell box ">
                                    <p>Iniciativa</p>
                                </div>
                            </div>
                        </div>
                        <div class="fixed-grid has-3-cols">
                            <div class="grid">
                                <div class=" box cell">
                                    <p>HP</p>
                                </div>
                                <div class=" box cell">
                                    <p>HP</p>
                                </div>
                                <div class="box cell">
                                    <p>HP</p>
                                </div>
                            </div>
                        </div>   
                    </div>
                </div>
        
                <div class="box"> 
                      
                </div>
                <div>
                    <h2 class="is-size-4">Acciones</h2>
                    <h2 class="is-size-5">Ataque con arma</h2>
                    <div class="grid has-5-cols is-centered">
                        
                        <table>
                            <thead>
                                <tr>
                                    <th>Arma</th>
                                    <th>Daño</th>
                                    <th>Rango</th> 
                                    <th>Critico</th>
                                    <th>Rango de Crítico</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th>Daga</th>
                                    <th>3</th>
                                    <th>1</th>
                                    <th>x4</th>
                                    <th>19/20</th>
                                </tr>
                            </tbody>
                        </table>

                        
                    </div>
                    <div>
                            <h2 class="is-size-4">Activas</h2>
                        </div>

                </div>
            </div>
            
            
           
            <div class="column is-2">
        <table class="table us-bordered is-striped is-narrow is-hoverable">
          <thead>
              <tr>
                  <th></th>
                  <th>Nombre</th>
                  <th>Atributo</th>
                  <th>Rangos</th>
                  <th>Bon. Varios</th>
                  <th>Total</th>
              </tr>
          </thead>  
          <tbody>
              <tr>
                  <td><input type="checkbox" id="atletismo" disabled></td>
                  <td>Atletismo</td>
                  <td class="body"></td>
                  <td><input type="number" value="" class="input1 input is-small mt-1"></td>
                  <td><input type="number" value="" class="input2 input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="nadar" disabled></td>
                  <td>Nadar</td>
                  <td class="body"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="aguante" disabled></td>
                  <td >Aguante</td>
                  <td class="body"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="medicina" disabled></td>
                  <td >Medicina</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="naturaleza" disabled></td>
                  <td>Naturaleza</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="geografia" disabled></td>
                  <td >Geografía</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="tasacion" disabled></td>
                  <td>Tasación</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="antropologia_politica" disabled></td>
                  <td>Política</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="historia" disabled></td>
                  <td>Historia</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="equitacion" disabled></td>
                  <td>Equitación</td>
                  <td class="agility"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="investigacion_buscar" disabled></td>
                  <td>Investigación</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="orientacion_navegacion" disabled></td>
                  <td>Orientación</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="percepcion" disabled></td>
                  <td>Percepción</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="supervivencia" disabled></td>
                  <td>Supervivencia</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="persuasion_dialectica" disabled></td>
                  <td>Persuasión</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="embaucar" disabled></td>
                  <td>Embaucar</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="intimidacion" disabled></td>
                  <td>Intimidar</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="averiguar_intenciones" disabled></td>
                  <td>Averiguar intenciones</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="performance" disabled></td>
                  <td>Performance</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="arte" disabled></td>
                  <td>Arte</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="sigilo" disabled></td>
                  <td>Sigilo</td>
                  <td class="agility"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="juego_de_manos" disabled></td>
                  <td>Juego de manos</td>
                  <td class="agility"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="acrobacias" disabled></td>
                  <td>Acrobacias</td>
                  <td class="agility"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
              <tr>
                  <td><input type="checkbox" id="falsificar_sabotear" disabled></td>
                  <td>Falsificar/Sabotear</td>
                  <td class="mind"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td><input type="number" value="" class="input is-small"></td>
                  <td class="output"></td>
              </tr>
          </tbody>
      </table>
            </div>
            
        </div>

    </div>
</template>


<script>
import axios from 'axios'
    export default {
        name: 'Character',
        data(){
            return {
                character: {},
            }
        },
        mounted() {
            this.getCharacter()
        },
        methods: {
            getCharacter(){
                const character_slug = this.$route.params.character_slug

                axios
                .get(`/api/v1/characters/${character_slug}`)
                .then(response => {
                    this.character = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }
</script>

<style scoped>
.table td, .table th {
  padding: 0.25rem; /* Reduce el padding entre columnas */
  margin:0.25;
}

input {
  font-size: 0.8rem; /* Reduce el tamaño de la fuente dentro de los inputs */
  padding: 0.2rem; /* Reduce el padding interno de los inputs */
  height: auto; /* Ajusta la altura para inputs pequeños */
  
}

.box {
  height: 50px; /* Alto uniforme */
  display: flex;
  align-items: center;
  text-align: center;
  padding: 0; /* Evita padding extra */
  padding-left: 2rem;
  overflow: hidden; /* Evita que el texto expanda el tamaño del contenedor */
  white-space: nowrap; /* Evita saltos de línea */
  text-overflow: ellipsis; /* Agrega "..." si el texto es demasiado largo */
}

</style>