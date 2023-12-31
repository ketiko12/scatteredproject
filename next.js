import {useRouter} from "next/router"

function Product({product}){
    const router= useRouter()
    if (router.isFallback){
        return <div>Page is loading...</div>
    }
    return(
       <div>
         <h2>{product.id} {product.title}</h2>
         <p>{product.description}</p>
         <hr/>
       </div>



    )
}

export default Product

export async function getStaticProps(context){
    const {params}= context;
    const response= await fetch(`http://localhost:4000/products/${params.productId}`)
     const data= response.json()
     return {
        props:{
            product:data
        }
     }    
}

export async function getStaticPaths(){
    return{
        paths:[
            {params:{productId:'1'}}
        ],
        fallback:true
        
    }
}
