<template>
<div id="menu">

<div class="container">
    <h3>Sandwiches</h3>
    <div class="row">
        <div class="col-md-3 mb-4" v-for="sand in sand" :key="sand.id">

            <div class="card h-100" style="width: 18rem;">
                <img :src="(sand.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ sand.title }}</h5>
                    <p class="card-text">{{ sand.description }}</p>
                    <p class="card-text mt-auto">{{ sand.calories }}</p>
                    <p class="card-text">{{ sand.price }}</p>
                </div>
            </div>
        </div>

        <h3>Salads</h3>

        <div class="col-md-3" v-for="sal in sal" :key="sal.id">

            <div class="card h-100 mb-4" style="width: 18rem;">
                <img :src="(sal.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ sal.title }}</h5>
                    <p class="card-text">{{ sal.description }}</p>
                    <p class="card-text mt-auto">{{ sal.calories }}</p>
                    <p class="card-text">{{ sal.price }}</p>
                </div>
            </div>
        </div>

        <h3>Wraps</h3>

        <div class="col-md-3" v-for="wrap in wrap" :key="wrap.id">

            <div class="card h-100 mb-4" style="width: 18rem;">
                <img :src="(wrap.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ wrap.title }}</h5>
                    <p class="card-text">{{ wrap.description }}</p>
                    <p class="card-text mt-auto">{{ wrap.calories }}</p>
                    <p class="card-text">{{ wrap.price }}</p>
                </div>
            </div>
        </div>

        <h3>Soup</h3>

        <div class="col-md-3" v-for="soup in soup" :key="soup.id">

            <div class="card h-100 mb-4" style="width: 18rem;">
                <img :src="(soup.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ soup.title }}</h5>
                    <p class="card-text">{{ soup.description }}</p>
                    <p class="card-text mt-auto">{{ soup.calories }}</p>
                    <p class="card-text">{{ soup.price }}</p>
                </div>
            </div>
        </div>

         <h3>Sides and Dressings</h3>

        <div class="col-md-3 mb-4" v-for="side in side" :key="side.id">

            <div class="card h-100" style="width: 18rem;">
                <img :src="(side.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ side.title }}</h5>
                    
                    <p class="card-text mt-auto">{{ side.calories }}</p>
                    <p class="card-text">{{ side.price }}</p>
                </div>
            </div>
        </div>

         <h3>Drinks</h3>

        <div class="col-md-3 mb-4" v-for="drink in drink" :key="drink.id">

            <div class="card h-100" style="width: 18rem;">
                <img :src="(drink.image)" class="card-img-top">
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">{{ drink.title }}</h5>
                    
                    <p class="card-text mt-auto">{{ drink.calories }}</p>
                    <p class="card-text">{{ drink.price }}</p>
                </div>
            </div>
        </div>
   
   
   
  
    
    <div class="">
        <div class="">

            <h3>lorem</h3>
            <h3>lorem</h3>
            <h3>lorem</h3>
            <h3>lorem</h3>
            <h3>lorem</h3>
            <h3>lorem</h3>
            <h3>lorem</h3>
        </div>
    </div>
     </div>


</div>

</div>
    
</template>



<script>
// import Sand from './Sand'
export default {
    name: "Menu",
//      components: {
//     Sand,
    
//   },
    data() {
        return {

            sand: [],
            sal: [],
            wrap: [],
            soup: [],
            side: [],
            drink: [],
            
        }
    },

    async created() {
        // const response = await fetch('http://localhost:8000/menu/sandwiches/');
        // this.sand = await response.json();

        Promise.all ([
            fetch('http://localhost:8000/menu/sandwiches/'),
            fetch('http://localhost:8000/menu/salads/'),
            fetch('http://localhost:8000/menu/wraps/'),
            fetch('http://localhost:8000/menu/soup/'),
            fetch('http://localhost:8000/menu/sides/'),
            fetch('http://localhost:8000/menu/drinks/'),
            

        ])
        .then(async([res1, res2, res3, res4, res5, res6]) => {
            this.sand = await res1.json();
            this.sal = await res2.json();
            this.wrap = await res3.json();
            this.soup = await res4.json();
            this.side = await res5.json();
            this.drink = await res6.json();
        })
    },

    methods: {
        
    }
}
</script>




<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.container {
    margin-top: 20px;
}


.container h3 {
    margin-top: 20px;
}


</style>

