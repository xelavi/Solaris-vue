<template>
  <div class="arbol-page">
    <v-network-graph
    class="graph"
    :nodes="nodes"
    :edges="edges"
    :layouts="layouts"
  />
  </div>
</template>

<script setup>

  import { VNetworkGraph } from "v-network-graph"
  import "v-network-graph/lib/style.css"
  const nodes = {
    node1: { name: "Node 1" },
    node2: { name: "Node 2" },
    node3: { name: "Node 3" },
   
  }

  const edges = {
    edge1: { source: "node1", target: "node3" },
    edge2: { source: "node2", target: "node3" },
  
  }

  const layouts = {
  nodes: {
    node1: { x: 0, y: 0 },
    node2: { x: 50, y: 0 },
    node3: { x: 25, y: -25 },
   
  },
  }
</script>
  
<style>
.graph {
  width: 800px;
  height: 600px;
  border: 1px solid #000;
}
</style>