import Layout from './components/layout'
import TimeSeriesChart from './components/time-series-chart'
import TwitterFollowersCard from './components/twitter-followers-card'

const App = () => {
  return (
    <Layout>
      <TwitterFollowersCard />
      <TimeSeriesChart />
    </Layout>
  );
}

export default App;
