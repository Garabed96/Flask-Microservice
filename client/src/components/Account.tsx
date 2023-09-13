import React, { useState, useEffect } from 'react'
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
export default function Account() {
   const [userData, setUserData] = useState({
      name: 'John Doe',
      email: 'John@example.com',
      membership_status: 'Basic',
      weight_value: '180',
      weight_unit: 'lbs',
      height_value: '6',
      height_unit: 'ft',
   })

   useEffect(() => {}, [])

   const [isEditMode, setIsEditMode] = useState(false)

   const handleEditButton = () => {
      setIsEditMode(!isEditMode)
   }

   const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      const { name, value } = e.target
      setUserData({ ...userData, [name]: value })
   }

   const handleSaveButton = () => {
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
               <Button ml={'8'} colorScheme="teal" onClick={handleSaveButton}>
                  Save
               </Button>
            ) : (
               <Button ml={'8'} colorScheme="teal" onClick={handleEditButton}>
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
                           <Th>Name</Th>
                           {isEditMode ? (
                              <Td maxWidth={'200px'}>
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
