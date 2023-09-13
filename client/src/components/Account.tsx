import React, { useState, useEffect, useCallback } from 'react'
import Navbar from './Navbar.tsx'
import { Center, Box, Text, Button } from '@chakra-ui/react'
import {
   Table,
   Thead,
   Tbody,
   Tr,
   Th,
   Td,
   TableCaption,
   TableContainer,
   Input,
} from '@chakra-ui/react'
import axios from 'axios'

// We're fetching random user data, on refresh we pull a new random user, we are only updating username with patch requests.
export default function Account() {
   const baseURL = 'http://127.0.0.1:8000'

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

   const [userData, setUserData] = useState({
      name: 'John Doe',
      email: 'John@example.com',
      membership_status: 'Basic',
      weight_value: 180,
      weight_unit: 'lbs',
      height_value: 6,
      height_unit: 'ft',
      id: 1,
   })

   const updateUser = useCallback(async (id: number, updatedUserData: User) => {
      try {
         // Send the updated data in the request body
         const response = await axios.patch(`${baseURL}/update/${id}`, updatedUserData)

         // Assuming the server responds with the updated user data
         const updatedUser = response.data

         // Update the local userData state with the new data
         setUserData(updatedUser)

         // Handle success or perform any necessary actions after updating.
         console.log('User updated successfully:', updatedUser)
      } catch (error) {
         // Handle errors if the request fails.
         console.error('Delete user failed:', error)
      }
   }, [])

   useEffect(() => {
      axios
         // .get(`${baseURL}/random_user`) // Use template literals
         .get(`${baseURL}/random_user`) // Use template literals
         .then((res) => {
            console.log(res.data)
            setUserData(res.data)
         })
         .catch((err) => {
            console.log(err)
         })
   }, [])

   const [isEditMode, setIsEditMode] = useState(false)

   const handleEditButton = () => {
      setIsEditMode(!isEditMode)
   }

   const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      const { name, value } = e.target
      setUserData({ ...userData, [name]: value })
   }

   const handleSaveButton = () => {
      const updatedUserData = {
         name: userData.name,
         email: userData.email,
         membership_status: userData.membership_status,
         weight_value: userData.weight_value,
         height_value: userData.height_value,
         id: userData.id,
         weight_unit: userData.weight_unit,
         height_unit: userData.height_unit,
      }

      // Call the updateUser function to send the updated data to the server
      updateUser(userData.id, updatedUserData)

      // Exit edit mode
      setIsEditMode(false)
   }

   return (
      <div>
         <Navbar />
         <Box mt="4rem">
            <Center>
               <Text m={'4'}>Account Page</Text>
            </Center>
            {isEditMode ? (
               <Button ml={'8'} mt={'4'} colorScheme="teal" onClick={handleSaveButton}>
                  Save
               </Button>
            ) : (
               <Button ml={'8'} mt={'4'} colorScheme="teal" onClick={handleEditButton}>
                  Edit
               </Button>
            )}
            <Box m={'8'} width="90%" display="flex" justifyContent="center">
               <TableContainer maxWidth={'90%'}>
                  <Table variant="simple" m={'8'} maxWidth={'90%'}>
                     <TableCaption>
                        Your user information, edit to change applicable information about yourself.
                     </TableCaption>
                     <Thead>
                        <Tr maxWidth={'100%'}>
                           <Th>Username</Th>
                           {isEditMode ? (
                              <Td>
                                 <Input
                                    maxWidth={'200px'}
                                    name="name"
                                    value={userData.name}
                                    onChange={handleInputChange}
                                 />
                              </Td>
                           ) : (
                              <Td>{userData.name}</Td>
                           )}
                        </Tr>
                     </Thead>
                     <Tbody>
                        <Tr>
                           <Td>Email:</Td>
                           {isEditMode ? (
                              <Td>
                                 <Input
                                    maxWidth={'200px'}
                                    name="email"
                                    value={userData.email}
                                    onChange={handleInputChange}
                                 />
                              </Td>
                           ) : (
                              <Td>{userData.email}</Td>
                           )}
                        </Tr>
                        <Tr>
                           <Td>Membership Status:</Td>
                           {isEditMode ? (
                              <Td>
                                 <Input
                                    maxWidth={'200px'}
                                    name="membership_status"
                                    value={userData.membership_status}
                                    onChange={handleInputChange}
                                 />
                              </Td>
                           ) : (
                              <Td>{userData.membership_status}</Td>
                           )}
                        </Tr>{' '}
                        <Tr>
                           <Td>Weight: </Td>
                           {isEditMode ? (
                              <Td>
                                 <Input
                                    maxWidth={'200px'}
                                    name="weight_value"
                                    value={userData.weight_value}
                                    onChange={handleInputChange}
                                 />
                              </Td>
                           ) : (
                              <Td>
                                 {userData.weight_value}
                                 {userData.weight_unit}
                              </Td>
                           )}
                        </Tr>
                        <Tr>
                           <Td>Height:</Td>
                           {isEditMode ? (
                              <Td>
                                 <Input
                                    maxWidth={'200px'}
                                    name="height_value"
                                    value={userData.height_value}
                                    onChange={handleInputChange}
                                 />
                              </Td>
                           ) : (
                              <Td>
                                 {userData.height_value}
                                 {userData.height_unit}
                              </Td>
                           )}
                        </Tr>{' '}
                        {/* Repeat similar structure for other user data fields */}
                     </Tbody>
                  </Table>
               </TableContainer>
            </Box>
         </Box>{' '}
      </div>
   )
}
