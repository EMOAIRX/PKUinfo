<!-- create a 404 not found page with daisy ui -->
<template>
  <div class="flex items-center justify-center h-screen">
    <div class="flex flex-col items-center justify-center">
      <h1 class="text-9xl font-bold text-error">404</h1>
      <h2 class="text-3xl font-semibold text-info">Page not found</h2>
      <router-link to="/" class="btn btn-primary mt-4">Go back home</router-link>
    </div>
  </div>
</template>