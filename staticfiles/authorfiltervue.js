var vue = new Vue({
    data: {
    list: [],
    sortOrder: "All"
  },
  created: function() {
    // simulating asynchronous loading of data
    setTimeout(() => {
  list = this.list;
    }, 1000);
  },
  mounted () {
    axios
      .get('../../api/author/')
      .then(response => (this.list = response.data))
      .catch(error => console.log(error))
      .finally(() => this.loading = false)
  },
  computed: {
    orderedListOptions: function() {
      var step;
      authors = this.list;
      return {
        All: () => {
          return authors;
        },
        A: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "A") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        B: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "B") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        C: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "C") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        D: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "D") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        E: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "E") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        F: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "F") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        G: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "G") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        H: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "H") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        I: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "I") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        J: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "J") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        K: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "K") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        L: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "L") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        M: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "M") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        N: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "N") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        O: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "O") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        P: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "P") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        Q: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "Q") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        R: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "R") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        S: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "S") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        T: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "T") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        U: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "U") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        V: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "V") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        W: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "W") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        X: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "X") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        Y: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "Y") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
        Z: () => {
          var step;
          let list1 = [];
          for (step = 0; step < authors.length; step++) {
            if (authors[step].last_name[0] == "Z") {
              list1.push(authors[step]);
            }
          }
          return list1;
        },
      };
    }
  },
  methods: {
    sort: function(sortOrder) {
      return this.orderedListOptions[sortOrder]();
    }
  },
  delimiters: ["<%","%>"],
  el: "#app"
});
