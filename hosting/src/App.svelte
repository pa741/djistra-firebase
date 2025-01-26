<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import viteLogo from "/vite.svg";
  import { getFirestore } from "firebase/firestore";
  import { initializeApp } from "firebase/app";
  import { FirebaseApp } from "sveltefire";
    import Map from "./lib/Map.svelte";
  const firebaseConfig = {
  // CONFIG
  };
  const app = initializeApp(firebaseConfig);
  const firestore = getFirestore(app);
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