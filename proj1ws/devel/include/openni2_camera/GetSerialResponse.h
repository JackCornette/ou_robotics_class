// Generated by gencpp from file openni2_camera/GetSerialResponse.msg
// DO NOT EDIT!


#ifndef OPENNI2_CAMERA_MESSAGE_GETSERIALRESPONSE_H
#define OPENNI2_CAMERA_MESSAGE_GETSERIALRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace openni2_camera
{
template <class ContainerAllocator>
struct GetSerialResponse_
{
  typedef GetSerialResponse_<ContainerAllocator> Type;

  GetSerialResponse_()
    : serial()  {
    }
  GetSerialResponse_(const ContainerAllocator& _alloc)
    : serial(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _serial_type;
  _serial_type serial;





  typedef boost::shared_ptr< ::openni2_camera::GetSerialResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::openni2_camera::GetSerialResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetSerialResponse_

typedef ::openni2_camera::GetSerialResponse_<std::allocator<void> > GetSerialResponse;

typedef boost::shared_ptr< ::openni2_camera::GetSerialResponse > GetSerialResponsePtr;
typedef boost::shared_ptr< ::openni2_camera::GetSerialResponse const> GetSerialResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::openni2_camera::GetSerialResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::openni2_camera::GetSerialResponse_<ContainerAllocator1> & lhs, const ::openni2_camera::GetSerialResponse_<ContainerAllocator2> & rhs)
{
  return lhs.serial == rhs.serial;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::openni2_camera::GetSerialResponse_<ContainerAllocator1> & lhs, const ::openni2_camera::GetSerialResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace openni2_camera

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::openni2_camera::GetSerialResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::openni2_camera::GetSerialResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::openni2_camera::GetSerialResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fca40cf463282a80db4e2037c8a61741";
  }

  static const char* value(const ::openni2_camera::GetSerialResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfca40cf463282a80ULL;
  static const uint64_t static_value2 = 0xdb4e2037c8a61741ULL;
};

template<class ContainerAllocator>
struct DataType< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "openni2_camera/GetSerialResponse";
  }

  static const char* value(const ::openni2_camera::GetSerialResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string serial\n"
"\n"
;
  }

  static const char* value(const ::openni2_camera::GetSerialResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.serial);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetSerialResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::openni2_camera::GetSerialResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::openni2_camera::GetSerialResponse_<ContainerAllocator>& v)
  {
    s << indent << "serial: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.serial);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OPENNI2_CAMERA_MESSAGE_GETSERIALRESPONSE_H
