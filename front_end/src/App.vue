<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="menu">Menu</router-link></li>
        <li><router-link to="nutrition">Nutrition</router-link></li>
        
        
        
      </ul>
    </nav>
    <router-view/>
  
  </div>

</template>

<script>


export default {
  name: 'App',
  data () {
    return {
      
    }
    
  },
}
</script>

<style>

body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #fffaf0;
}

nav {

  display: flex;
  justify-content: space-around;
  align-items: center;
  min-height: 8vh;
  background-color: #66cdaa;

}
nav ul {
  display: flex;
  justify-content: space-around;
  width: 30%;
  text-decoration: none;
  list-style-type: none;
}

li a {
  text-decoration: none;
  letter-spacing: 2px;
  font-weight: bold;
  font-size: 16px;
  color: #fdf5e6;

 
}

li :hover{
  color: #fbecd0;


}

</style>
