import React, { useEffect, useState } from 'react'

const TwitterFollowersCard = () => {

    const [followers, setFollowers] = useState();

    useEffect(() => {
        fetch('http://127.0.0.1:5000/twitterfollowers?as_of_date=2020-11-10', 
        {
            method: "GET"
        })
        .then(res => res.json())
        .then(response => {setFollowers(response.followers)})
    })

    return(
        <div>
            {followers}
        </div>
    )
}

export default TwitterFollowersCard