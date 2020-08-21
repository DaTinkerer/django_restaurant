<template>
<div id="menu">
     <div class="container  sticky-top">
          <nav class="navbar navbar-dark bg-white">
                <ul class="container-fluid">
                    <li><h5 @click="goTo('sand')">Sandwiches</h5></li>
                    <li><h5 @click="goTo('sal')">Salads</h5></li>
                    <li><h5 @click="goTo('wrap')">Wraps</h5></li>
                    <li><h5 @click="goTo('soup')">Soup</h5></li>
                    <li><h5 @click="goTo('side')">Sides and Dressings</h5></li>
                    <li><h5 @click="goTo('drink')">Drinks</h5></li>
                </ul>
            </nav>
    </div>
       

    <div class="container">
        <h3 ref="sand">Sandwiches</h3>
        <div class="row">
            <div class="col-md-3 mb-4" v-for="sand in sand" :key="sand.id">

                <div class="card h-100" style="width: 18rem;">
                    <img :src="(sand.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ sand.title }}</h5>
                        <p class="card-text">{{ sand.description }}</p>
                        <p class="card-text mt-auto">{{ sand.calories }} Cal</p>
                        <p class="card-text">&#36;{{ sand.price }}</p>
                    </div>
                </div>
            </div>
             
            


            <h3 ref="sal">Salads</h3>

            <div class="col-md-3" v-for="sal in sal" :key="sal.id">

                <div class="card h-100 mb-4" style="width: 18rem;">
                    <img :src="(sal.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ sal.title }}</h5>
                        <p class="card-text">{{ sal.description }}</p>
                        <p class="card-text mt-auto">{{ sal.calories }} Cal</p>
                        <p class="card-text">&#36;{{ sal.price }}</p>
                    </div>
                </div>
            </div>

            <h3 ref="wrap">Wraps</h3>

            <div class="col-md-3" v-for="wrap in wrap" :key="wrap.id">

                <div class="card h-100 mb-4" style="width: 18rem;">
                    <img :src="(wrap.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ wrap.title }}</h5>
                        <p class="card-text">{{ wrap.description }}</p>
                        <p class="card-text mt-auto">{{ wrap.calories }} Cal</p>
                        <p class="card-text">&#36;{{ wrap.price }}</p>
                    </div>
                </div>
            </div>

            <h3 ref="soup">Soup</h3>

            <div class="col-md-3" v-for="soup in soup" :key="soup.id">

                <div class="card h-100 mb-4" style="width: 18rem;">
                    <img :src="(soup.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ soup.title }}</h5>
                        <p class="card-text">{{ soup.description }}</p>
                        <p class="card-text mt-auto">{{ soup.calories }} Cal</p>
                        <p class="card-text">&#36;{{ soup.price }}</p>
                    </div>
                </div>
            </div>

            <h3 ref="side">Sides and Dressings</h3>

            <div class="col-md-3 mb-4" v-for="side in side" :key="side.id">

                <div class="card h-100" style="width: 18rem;">
                    <img :src="(side.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ side.title }}</h5>
                        
                        <p class="card-text mt-auto">{{ side.calories }} Cal</p>
                        <p class="card-text">&#36;{{ side.price }}</p>
                    </div>
                </div>
            </div>

            
            <h3 ref="drink">Drinks</h3>
            <div class="col-md-3 mb-4" v-for="drink in drink" :key="drink.id">

                <div class="card h-100" style="width: 18rem;">
                    <img :src="(drink.image)" class="card-img-top">
                    <div class="card-body d-flex flex-column">
                        <h5 class="card-title">{{ drink.title }}</h5>
                        
                        <p class="card-text mt-auto">{{ drink.calories }} Cal</p>
                        <p class="card-text">&#36;{{ drink.price }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

   

</div>
    
</template>



<script>

export default {
    name: "Menu",
     components: {
    
    
  },
    data() {
        return {
            // list rendering
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
            if (res1.status >= 200 && res1.status <= 299) {
                this.sand = await res1.json();
                this.sal = await res2.json();
                this.wrap = await res3.json();
                this.soup = await res4.json();
                this.side = await res5.json();
                this.drink = await res6.json();
            } else {

                throw Error(res1.statusText)

            }
        })
    },

    methods: {

        goTo (refName) {
            var element = this.$refs[refName];
          element.scrollIntoView({ behavior: 'smooth'});
        }
        
    }
}
</script>




<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}




.container h3 {
    margin-top: 20px;
}

nav li h5 {
    color: gray;
    cursor:pointer;
}

.container li :hover{
    color: black;
}



</style>

