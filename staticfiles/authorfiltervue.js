function genCharArray(charA, charZ) {
    var a = [], i = charA.charCodeAt(0), j = charZ.charCodeAt(0);
    for (; i <= j; ++i) {
        a.push(String.fromCharCode(i));
    }
    return a;
}

Vue.filter('startsWith', function (array, search, field) {
  if (!search.length) return array;
  
  return array.filter(function(element) {
    return element[field].toLowerCase().indexOf(search.toLowerCase()) === 0;
  })
})

new Vue({
  el: '#main',
  delimiters: ["<%","%>"],
  data () {
    return {
      authorsList: [],
      selectedLetter: undefined,
      authors: {},
      loading: true,
      errored: false,
      sortOrder: "All",
      letterFilter: 0,
    }
  },
  mounted () {
    axios
      .get('../../api/author/')
      .then(response => (this.authors = response.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
  },
  created () {
    this.alphabet = genCharArray('a','z')
  },
  computed : {
    AuthorsList() {
      var step;
      let authors = this.authors;
      let authorsList = [];
      for (var step = 0; step < authors.length; step++) {
        authorsList.push(authors[step].last_name);
      };
      if (this.selectedLetter) {
        authorsList = authorsList.filter((name) => {
          let firstLetter = name.charAt(0).toLowerCase()
          return firstLetter === this.selectedLetter
        })
      }
    return authorsList;
  }
  },
  filters : {
    letterFilter(value) {
      var step;
      let authorsList = [];
      let filtered = [];
      for (var step = 0; step < authorsList.length; step++) {
        if(authorsList[step].charAt(0) == value) {
          filtered.push(authorList[step]);
        }
      return filtered;
      }
    },
  }
})