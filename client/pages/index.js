import { useState } from 'react'

export default function Home() {
  const [data, setData] = useState(null)
  const [isLoading, setLoading] = useState(false)

  const fetchData = async (code) => {
    setLoading(true)
    await fetch('http://127.0.0.1:5000/2680')
      .then((res) => res.json())
      .then((data) => {
        setData(data)
        setLoading(false)
      })
  }

  return (
    <div className="w-screen h-screen">
      <div className="grid grid-cols-2 gap-x-10 w-full">
        <div className="w-4/6">
          <input type="text" className="border-solid border-2 border-black focus:outline-none w-4/6" required />
        </div>

        <button className="w-20" onClick={fetchData}>Get</button>
      </div>

      <div className='mx-[10%] prose lg:prose-lg prose-a:text-blue-700 max-w-none prose-headings:text-center'>
        {data !== null ? <div dangerouslySetInnerHTML={{ __html: data.html }} /> : ""}
      </div>
    </div>
  )
}