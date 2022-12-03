const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data(){
        return{
        message: 'hello world'
        }
    },
    methods: {
        loadBooks(){
        },
    },
    mounted(){
       this.csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value
      
       
    }
})

