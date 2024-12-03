<template>
<div class="background-page">
        
        <div class="fixed-grid has-6-cols ">
            <div class="grid">
                <div class="cell is-col-start-3 mb-6 mt-6">
                    <h1 class="title">Trasfondo</h1>
                </div>
                
                <div class="cell is-col-start-3 mt-3">
                    <h2 class="subtitle is-size-3">Nombre</h2>
                    
                </div>

                <div class="cell is-col-start-3 mt-5 mb-4 box">
                    <p class="is-size-5">Nodo 1:</p>
                    <p class="is-size-5">Nodo 2:</p>
                </div>
                    <div class="cell is-col-start-3">
                        <h2 class="subtitle">Elige 3 habilidades</h2>
                       <div class="fixed-grid has-2-cols">
                        <div class="grid col-start-1 mt-3">
                        <input type="checkbox"> <p>Habilidad 1</p>
                        <input type="checkbox"> <p>Habilidad 1</p>
                        <input type="checkbox"> <p>Habilidad 1</p>
                        <input type="checkbox"> <p>Habilidad 1</p>
                        <input type="checkbox"> <p>Habilidad 1</p>
                        <input type="checkbox"> <p>Habilidad 1</p>
                        </div>

                       </div>
                    </div>
                    
                    
                
                    <div class="buttons cell is-col-start-3 ">
                <router-link to="/create-character/arbol" class="button is-info">Siguiente</router-link>
                </div>
              

                </div>
            </div>
    
    </div>
</template>

<script>
 export default {
    name: 'Background'
 }
</script>