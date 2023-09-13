import { Table, Thead, Tbody, Tr, Th, Td, TableCaption, TableContainer } from '@chakra-ui/react'
import { useEffect, useState } from 'react'
import axios from 'axios'
export default function AdminTable() {
   interface User {
      name: string
      email: string
      membership_status: string
      weight_value: number
      height_value: number
      weight_unit: string
      height_unit: string
      id: number
   }

   const [userData, setUserData] = useState<User[]>([])

   const baseURL = 'http://127.0.0.1:8000'
   useEffect(() => {
      axios
         .get(`${baseURL}/all`) // Use template literals
         .then((res) => {
            console.log(userData.length)
            console.log(res.data.users)
            setUserData(res.data.users)
         })
         .catch((err) => {
            console.log(err)
         })
   }, [])

   return (
      <TableContainer>
         <Table variant="simple">
            <TableCaption>User List Admin Panel</TableCaption>
            <Thead>
               <Tr>
                  <Th>Email</Th>
                  <Th>Name</Th>
                  <Th>Height</Th>
                  <Th>Weight</Th>
                  <Th>Membership Status</Th>
               </Tr>
            </Thead>
            <Tbody>
               {userData.length === 0 ? (
                  <Tr>
                     <Td>Email</Td>
                     <Td>Name</Td>
                     <Td>Name</Td>
                     <Td>Weight</Td>
                     <Th>Membership Status</Th>
                  </Tr>
               ) : (
                  userData.map((user) => (
                     <Tr key={user.id}>
                        <Td>{user.email}</Td>
                        <Td>{user.name}</Td>
                        <Td>
                           {user.height_value}
                           {user.height_unit}
                        </Td>
                        <Td>
                           {user.weight_value}
                           {user.weight_unit}
                        </Td>
                        <Td>{user.membership_status}</Td>
                     </Tr>
                  ))
               )}
            </Tbody>
         </Table>
      </TableContainer>
   )
}
