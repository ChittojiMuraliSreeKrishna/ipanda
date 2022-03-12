import './App.css';

export function App({ data }) {

  const domains = data.domains;

  return (
    <div className="App">
      <h2>{domains[0].title}</h2>
    </div>
  );
}

export function getStaticProps() {
  return {
    props: {
      data: {
        domains: [{ title: "Textile" }],
      },
    },
  };
}