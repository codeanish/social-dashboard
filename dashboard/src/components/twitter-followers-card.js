import React, { useEffect, useState } from 'react'
import styled from 'styled-components'



const TwitterFollowersCard = () => {

    const [followers, setFollowers] = useState();

    const StyledCard = styled.div`
    background-image: linear-gradient(to top right, #3020D3, #1F1596); 
    color: white;
    width: 200px;
    height: 100px;
    border-radius: 5px;
`

    useEffect(() => {
        fetch('http://127.0.0.1:5000/twitterfollowers?as_of_date=2020-11-13', 
        {
            method: "GET"
        })
        .then(res => res.json())
        .then(response => {setFollowers(response.followers)})
    })

    var containerStyle={
        display: 'flex',
        flexDirection: 'column',
        padding: '10px',                
        textAlign: 'center'
    }

    var countStyle={
        fontSize: '48px'        
    }

    var socialStyle={
        fontSize: '20px'
    }


    return(
        <div>
            <StyledCard>
                <div style={containerStyle}>
                    <div style={socialStyle}>Twitter</div>                    
                    <div style={countStyle}>{followers}</div>
                </div>
            </StyledCard>            
        </div>
    )
}

export default TwitterFollowersCard