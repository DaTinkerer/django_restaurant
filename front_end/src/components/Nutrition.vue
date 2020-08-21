<template>
    <div id="nutrition">
        <div class="container">
          <nav class="navbar navbar-dark bg-white">
                <ul class="container-fluid">
                    <li v-on:click="breads = true; tortilla = false; lettuce = false"><h5>Sandwiches</h5></li>
                    <li v-on:click="lettuce = true; breads = false; true; tortilla = false"><h5>Salads</h5></li>
                    <li v-on:click="tortilla = true; lettuce = false; breads = false "><h5>Wraps</h5></li>
                    
                </ul>
            </nav>
    </div>

    <div class="container">

        <h3 v-show="breads">Breads</h3>
        <div class="row">
            <div v-show="breads" class="col-md-3 mb-3 mt-3" v-for="bread in bread" :key="bread.id">
                <div class="card">
                    <div class="card-body">
                        <p>{{ bread.title }}</p>
                        <p>{{ bread.calories }} Cal</p>
                        <!-- <div class="btn-group" role="group" aria-label="Basic example">
                            <button v-on:click="subTotal(bread.calories)"  type="button" class="btn btn-secondary">-</button>
                            <button v-on:click="addTotal(bread.calories)"  type="button" class="btn btn-secondary">+</button>
                            
                        </div> -->
                    </div>
                </div>
            </div>

            <h3 v-show="lettuce">Lettuce</h3>

            <div v-show="lettuce" class="col-md-3 mb-3 mt-3" v-for="lett in lett" :key="lett.id">
                <div class="card">
                    <div class="card-body">
                        <p>{{ lett.title }}</p>
                        <p>{{ lett.calories }} Cal</p>
                    </div>
                </div>
            </div>

            <h3 v-show="tortilla">Tortillas</h3>

            <div v-show="tortilla" class="col-md-3 mb-3 mt-3" v-for="tort in tort" :key="tort.id">
                <div class="card">
                    <div class="card-body">
                        <p>{{ tort.title }}</p>
                        <p>{{ tort.calories }} Cal</p>
                    </div>
                </div>
            </div>

            <h3>Protein</h3>

            <div class="col-md-3 mb-3 mt-3" v-for="prot in prot" :key="prot.id">
                <div class="card">
                    <div class="card-body">
                        <p>{{ prot.title }}</p>
                        <p>{{ prot.calories }} Cal</p>
                    </div>
                </div>
            </div>

            <h3>Toppings</h3>

            <div class="col-md-3 mb-3 mt-3" v-for="top in top" :key="top.id">
                <div class="card">
                    <div class="card-body">
                        <p>{{ top.title }}</p>
                        <p>{{ top.calories }} Cal</p>
                    </div>
                </div>
            </div>
        </div>

        
    </div>

    

    </div>
</template>



<script>
export default {
    name: 'Nutrition',

    data () {
        return {
            // list rendering
            bread: [],
            top: [],
            lett: [],
            prot: [],
            tort: [],

        
            
            // conditionals
            breads : true,
            lettuce: false,
            tortilla: false,

            // Calorie Total
            cal_total: 0,
            count: 1,

        }

        
    },

    async created () {

        Promise.all ([
            fetch('http://localhost:8000/menu/breads/'),
            fetch('http://localhost:8000/menu/toppings/'),
            fetch('http://localhost:8000/menu/lettuce/'),
            fetch('http://localhost:8000/menu/protein/'),
            fetch('http://localhost:8000/menu/tortillas/'),
            
            

        ])
        .then(async([res1, res2, res3, res4, res5]) => {
            this.bread = await res1.json();
            this.top = await res2.json();
            this.lett = await res3.json();
            this.prot = await res4.json();
            this.tort = await res5.json();
        
            

    })
    },

    methods: {

        // addTotal (newCal) {
        //     if (this.count % 2 != 0) {
        //     var current_cal = this.cal_total;
        //     this.cal_total = current_cal + newCal;
        //     this.count++;
            
            
        //     } else {
                
        //         this.cal_total = this.cal_total - newCal;
        //         this.count++;
                


        //     }
            
        // },

        // subTotal (newCal) {

        //     const current_cal = this.cal_total;
        //     this.cal_total = current_cal - newCal;

        //     if (this.cal_total < 0) {
        //         this.cal_total = 0;
        //     }

            

            
        // }


    },
}
</script> 