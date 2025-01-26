<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import viteLogo from "/vite.svg";
  import { getFirestore } from "firebase/firestore";
  import { initializeApp } from "firebase/app";
  import { FirebaseApp } from "sveltefire";
    import Map from "./lib/Map.svelte";
  const firebaseConfig = {
    apiKey: "AIzaSyCiqLoieK5L5NzoPSbPYBUAykPx6z1isTc",
    authDomain: "algoritmo-rutas-entrega.firebaseapp.com",
    projectId: "algoritmo-rutas-entrega",
    storageBucket: "algoritmo-rutas-entrega.firebasestorage.app",
    messagingSenderId: "165699404263",
    appId: "1:165699404263:web:0c033c0308612980e7fd42",
    measurementId: "G-JYWZEM8ZSC",
  };
  const app = initializeApp(firebaseConfig);
  const firestore = getFirestore(app);
//9AzDlyCvfhMjvdcFnJNT	
</script>

<div class="app">
<FirebaseApp firestore={firestore}>
  <Map />
</FirebaseApp>

</div>

<style>
  .app {
    text-align: center;
  }
</style>