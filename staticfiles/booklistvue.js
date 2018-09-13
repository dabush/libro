new Vue({
  el: '#main',
  delimiters: ["<%","%>"],
  data () {
    return {
      searchString: "",
      books: null,
      searchArray: {},
      loading: true,
      errored: false
    }
  },
  mounted () {
    axios
      .get('../../api/book/')
      .then(response => (this.books = response.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
  },
  computed : {
        // A computed property that holds only those data that match the searchString.
        filteredData: function () {
                var searchArray = this.books,
                searchString = this.searchString;

            if(!searchString){
                return searchArray;
            }

            searchString = searchString.trim().toLowerCase();

            searchArray = searchArray.filter(item => {
                if(item.book_title.toLowerCase().indexOf(searchString) !== -1){
                    return item;
                }
            })

            // Return an array with the filtered data.
            return searchArray;
        }
    },
})


